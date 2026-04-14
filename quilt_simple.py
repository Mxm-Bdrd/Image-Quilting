import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import fftconvolve


def SDC(template, sample, mask):
    out_h = sample.shape[0] - template.shape[0] + 1
    out_w = sample.shape[1] - template.shape[1] + 1
    ssd = np.zeros((out_h, out_w))

    for c in range(sample.shape[2]):
        T_c = template[:, :, c]
        S_c = sample[:, :, c]
        M_c = mask[:, :, c]
        T_flip = np.rot90(T_c, 2)
        M_flip = np.rot90(M_c, 2)
        term1 = np.sum(M_c * (T_c ** 2))
        term2 = -2 * fftconvolve(S_c, M_flip * T_flip, mode='valid')
        term3 = fftconvolve(S_c ** 2, M_flip, mode='valid')
        ssd += (term1 + term2 + term3)

    ssd[ssd < 0] = 0
    return ssd


def quilt_simple(sample, outsize, patchsize, overlap, tol):
    out_h, out_w = outsize
    sample_h, sample_w, channels = sample.shape
    output = np.zeros((out_h, out_w, channels), dtype=np.float64)
    step = patchsize - overlap

    for i in range(0, out_h, step):
        for j in range(0, out_w, step):
            h_max = min(patchsize, out_h - i)
            w_max = min(patchsize, out_w - j)

            if i == 0 and j == 0:
                y = np.random.randint(0, sample_h - patchsize + 1)
                x = np.random.randint(0, sample_w - patchsize + 1)
                patch = sample[y:y + patchsize, x:x + patchsize]

            else:
                mask = np.zeros((patchsize, patchsize, channels), dtype=np.float64)
                template = np.zeros((patchsize, patchsize, channels), dtype=np.float64)
                if i > 0:
                    overlap_h = min(overlap, h_max)
                    mask[:overlap_h, :w_max, :] = 1
                    template[:overlap_h, :w_max, :] = output[i:i + overlap_h, j:j + w_max, :]
                if j > 0:
                    overlap_w = min(overlap, w_max)
                    mask[:h_max, :overlap_w, :] = 1
                    template[:h_max, :overlap_w, :] = output[i:i + h_max, j:j + overlap_w, :]

                ssd = SDC(template, sample, mask)
                minc = np.min(ssd)
                minc = max(minc, 1e-5)

                y_indices, x_indices = np.where(ssd <= minc * (1.0 + tol))
                choice = np.random.randint(len(y_indices))
                y = y_indices[choice]
                x = x_indices[choice]
                patch = sample[y:y + patchsize, x:x + patchsize]

            output[i:i + h_max, j:j + w_max] = patch[:h_max, :w_max]

    return output


if __name__ == '__main__':
    sample = plt.imread('textures/vitre.png')
    if sample.dtype == np.uint8:
        sample = sample.astype(np.float64) / 255.0
    if sample.shape[2] == 4:
        sample = sample[:, :, :3]

    outsize = (300, 300)
    patchsize = 31
    overlap = 7
    tol = 0.1

    resultat_p2 = quilt_simple(sample, outsize, patchsize, overlap, tol)
    plt.imsave("P2/vitre.png", np.clip(resultat_p2, 0, 1))

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(sample)
    axes[0].set_title("Texture Originale")
    axes[0].axis('off')
    axes[1].imshow(np.clip(resultat_p2, 0, 1))
    axes[1].set_title(f"Chevauchement simple")
    axes[1].axis('off')
    plt.tight_layout()
    plt.show()