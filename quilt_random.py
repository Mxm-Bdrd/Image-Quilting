import numpy as np
import matplotlib.pyplot as plt


def quilt_random(sample, outsize, patchsize):
    out_h, out_w = outsize
    sample_h, sample_w, channels = sample.shape
    output = np.zeros((out_h, out_w, channels), dtype=sample.dtype)

    for i in range(0, out_h, patchsize):
        for j in range(0, out_w, patchsize):
            y = np.random.randint(0, sample_h - patchsize + 1)
            x = np.random.randint(0, sample_w - patchsize + 1)
            patch = sample[y:y + patchsize, x:x + patchsize]

            h_to_copy = min(patchsize, out_h - i)
            w_to_copy = min(patchsize, out_w - j)
            output[i:i + h_to_copy, j:j + w_to_copy] = patch[:h_to_copy, :w_to_copy]

    return output


if __name__ == '__main__':
        img = plt.imread('textures/vitre.png')
        if img.dtype == np.uint8:
            img = img.astype(np.float64) / 255.0

        taille_sortie = (500, 500)
        taille_bloc = 50
        resultat = quilt_random(img, taille_sortie, taille_bloc)
        plt.imsave('P1/vitre.png', resultat)

        fig, axes = plt.subplots(1, 2, figsize=(10, 5))
        axes[0].imshow(img)
        axes[0].set_title("Texture d'entrée")
        axes[0].axis('off')
        axes[1].imshow(resultat)
        axes[1].set_title("Synthèse aléatoire")
        axes[1].axis('off')
        plt.tight_layout()
        plt.show()