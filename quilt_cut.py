import numpy as np
import matplotlib.pyplot as plt
from quilt_simple import SDC


def cut(bndcost):
    r, c = bndcost.shape
    cost = np.zeros_like(bndcost)
    cost[0, :] = bndcost[0, :]
    paths = np.zeros((r, c), dtype=int)

    for i in range(1, r):
        for j in range(c):
            start = max(0, j - 1)
            end = min(c, j + 2)
            min_idx = np.argmin(cost[i - 1, start:end])
            cost[i, j] = bndcost[i, j] + cost[i - 1, start + min_idx] # Pour update
            paths[i, j] = start + min_idx

    mask = np.zeros_like(bndcost)
    j = np.argmin(cost[-1, :])
    for i in range(r - 1, -1, -1):
        mask[i, j:] = 1
        j = paths[i, j]
    return mask


def quilt_cut(sample, outsize, patchsize, overlap, tol):
    out_h, out_w = outsize
    sample_h, sample_w, channels = sample.shape
    output = np.zeros((out_h, out_w, channels), dtype=np.float64)
    step = patchsize - overlap

    for i in range(0, out_h, step):
        for j in range(0, out_w, step):
            h_max = min(patchsize, out_h - i)
            w_max = min(patchsize, out_w - j)
            if i == 0 and j == 0: # Trouve blocs
                y = np.random.randint(0, sample_h - patchsize + 1)
                x = np.random.randint(0, sample_w - patchsize + 1)
                nouveau_patch = sample[y:y + patchsize, x:x + patchsize]
                output[i:i + h_max, j:j + w_max] = nouveau_patch[:h_max, :w_max]
                continue
            mask_search = np.zeros((patchsize, patchsize, channels), dtype=np.float64)
            template = np.zeros((patchsize, patchsize, channels), dtype=np.float64)

            if i > 0:
                overlap_h = min(overlap, h_max)
                mask_search[:overlap_h, :w_max, :] = 1
                template[:overlap_h, :w_max, :] = output[i:i + overlap_h, j:j + w_max, :]
            if j > 0:
                overlap_w = min(overlap, w_max)
                mask_search[:h_max, :overlap_w, :] = 1
                template[:h_max, :overlap_w, :] = output[i:i + h_max, j:j + overlap_w, :]

            ssd = SDC(template, sample, mask_search)
            minc = max(np.min(ssd), 1e-5)
            y_indices, x_indices = np.where(ssd <= minc * (1.0 + tol))
            choice = np.random.randint(len(y_indices))
            y = y_indices[choice]
            x = x_indices[choice]

            nouveau_patch = sample[y:y + patchsize, x:x + patchsize]
            masque_final = np.ones((h_max, w_max), dtype=np.float64)

            if i > 0:
                overlap_h = min(overlap, h_max)
                old_region = output[i:i + overlap_h, j:j + w_max]
                new_region = nouveau_patch[:overlap_h, :w_max]
                err_top = np.sum((old_region - new_region) ** 2, axis=2) #SDC
                mask_top_overlap = cut(err_top.T).T

                full_mask_top = np.ones((h_max, w_max), dtype=np.float64)
                full_mask_top[:overlap_h, :] = mask_top_overlap
                masque_final = masque_final * full_mask_top

            if j > 0:
                overlap_w = min(overlap, w_max)
                old_region = output[i:i + h_max, j:j + overlap_w]
                new_region = nouveau_patch[:h_max, :overlap_w]

                err_left = np.sum((old_region - new_region) ** 2, axis=2)
                mask_left_overlap = cut(err_left)
                full_mask_left = np.ones((h_max, w_max), dtype=np.float64)
                full_mask_left[:, :overlap_w] = mask_left_overlap
                masque_final = masque_final * full_mask_left

            final_mask_3d = np.repeat(masque_final[:, :, np.newaxis], channels, axis=2) # couleurs
            old_patch_full = output[i:i + h_max, j:j + w_max]
            new_patch_full = nouveau_patch[:h_max, :w_max]
            output[i:i + h_max, j:j + w_max] = (final_mask_3d * new_patch_full) + ((1 - final_mask_3d) * old_patch_full)

    return output


if __name__ == '__main__':
    sample = plt.imread("textures/vitre.png")
    if sample.dtype == np.uint8:
        sample = sample.astype(np.float64) / 255.0

    outsize = (300, 300)
    patchsize = 31
    overlap = 7
    tol = 0.1

    resultat_p3 = quilt_cut(sample, outsize, patchsize, overlap, tol)
    plt.imsave("P3/vitre.png", np.clip(resultat_p3, 0, 1))
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(sample)
    axes[0].set_title("Texture Originale")
    axes[0].axis('off')
    axes[1].imshow(np.clip(resultat_p3, 0, 1))
    axes[1].set_title("Coupe optimale (Seam Carving)")
    axes[1].axis('off')
    plt.tight_layout()
    plt.show()