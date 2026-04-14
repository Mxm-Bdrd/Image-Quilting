import numpy as np
import matplotlib.pyplot as plt
from quilt_simple import SDC
from quilt_cut import cut


def texture_transfer(sample, target, patchsize, overlap, tol, alpha):
    out_h, out_w, channels = target.shape
    sample_h, sample_w, _ = sample.shape
    output = np.zeros((out_h, out_w, channels), dtype=np.float64)
    step = patchsize - overlap

    for i in range(0, out_h, step):
        for j in range(0, out_w, step):

            h_max = min(patchsize, out_h - i)
            w_max = min(patchsize, out_w - j)

            target_patch = target[i:i + h_max, j:j + w_max]
            template_target = np.zeros((patchsize, patchsize, channels), dtype=np.float64)
            mask_target = np.zeros((patchsize, patchsize, channels), dtype=np.float64)
            template_target[:h_max, :w_max] = target_patch
            mask_target[:h_max, :w_max] = 1.0
            ssd_target = SDC(template_target, sample, mask_target)

            template_overlap = np.zeros((patchsize, patchsize, channels), dtype=np.float64)
            mask_overlap = np.zeros((patchsize, patchsize, channels), dtype=np.float64)

            if i > 0: #overlap
                overlap_h = min(overlap, h_max)
                mask_overlap[:overlap_h, :w_max, :] = 1.0
                template_overlap[:overlap_h, :w_max, :] = output[i:i + overlap_h, j:j + w_max, :]
            if j > 0:
                overlap_w = min(overlap, w_max)
                mask_overlap[:h_max, :overlap_w, :] = 1.0
                template_overlap[:h_max, :overlap_w, :] = output[i:i + h_max, j:j + overlap_w, :]

            if i == 0 and j == 0:
                sdc_overlap = np.zeros_like(ssd_target)
            else:
                sdc_overlap = SDC(template_overlap, sample, mask_overlap)

            sdc_total = (alpha * sdc_overlap) + ((1.0 - alpha) * ssd_target)
            minc = max(np.min(sdc_total), 1e-5)
            y_indices, x_indices = np.where(sdc_total <= minc * (1.0 + tol))
            choix = np.random.randint(len(y_indices))
            y = y_indices[choix]
            x = x_indices[choix]

            nouveau_patch = sample[y:y + patchsize, x:x + patchsize]
            masque_final = np.ones((h_max, w_max), dtype=np.float64)

            if i > 0:
                overlap_h = min(overlap, h_max)
                err_top = np.sum((output[i:i + overlap_h, j:j + w_max] - nouveau_patch[:overlap_h, :w_max]) ** 2, axis=2)
                mask_top = cut(err_top.T).T
                full_mask_top = np.ones((h_max, w_max), dtype=np.float64)
                full_mask_top[:overlap_h, :] = mask_top
                masque_final = masque_final * full_mask_top

            if j > 0:
                overlap_w = min(overlap, w_max)
                err_left = np.sum((output[i:i + h_max, j:j + overlap_w] - nouveau_patch[:h_max, :overlap_w]) ** 2, axis=2)
                mask_left = cut(err_left)
                full_mask_left = np.ones((h_max, w_max), dtype=np.float64)
                full_mask_left[:, :overlap_w] = mask_left
                masque_final = masque_final * full_mask_left

            final_mask_3d = np.repeat(masque_final[:, :, np.newaxis], channels, axis=2)
            output[i:i + h_max, j:j + w_max] = (final_mask_3d * nouveau_patch[:h_max, :w_max]) + (
                        (1 - final_mask_3d) * output[i:i + h_max, j:j + w_max])

    return output


if __name__ == '__main__':

    texture = plt.imread('textures/white_small.jpg')
    cible = plt.imread('personnelles/mog.png')

    if texture.dtype == np.uint8:
        texture = texture.astype(np.float64) / 255.0
    if texture.shape[2] == 4:
        texture = texture[:, :, :3]
    if cible.dtype == np.uint8:
        cible = cible.astype(np.float64) / 255.0
    if cible.shape[2] == 4:
        cible = cible[:, :, :3]

    patchsize = 31
    overlap = 9
    tol = 0.1
    alpha = 0.01 # entre 0 et 1, 1 ignore cible

    resultat_p4 = texture_transfer(texture, cible, patchsize, overlap, tol, alpha)
    plt.imsave("P5/Oli.png", np.clip(resultat_p4, 0, 1))

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    axes[0].imshow(texture)
    axes[0].set_title("Texture Source")
    axes[0].axis('off')
    axes[1].imshow(cible)
    axes[1].set_title("Image Cible")
    axes[1].axis('off')
    axes[2].imshow(np.clip(resultat_p4, 0, 1))
    axes[2].set_title(f"Transfert (alpha={alpha})")
    axes[2].axis('off')
    plt.tight_layout()
    plt.show()