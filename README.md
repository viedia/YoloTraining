# YoloTraining

Gabriel Masson

---

# Fonctions

### def predict()

#### Permet de lancer l'analyse d'une image

<blockquote>

Ne pas oublier de bien de mettre de le bon chemin d'accès d'une image.

</blockquote>

<p>&nbsp;</p>

### def exportONNX()

#### Permet d'exporter un model en format ONNX

<blockquote>

Ne pas oublier de bien charger le model avant.

</blockquote>

<p>&nbsp;</p>

### def learning()

#### Permet de lancer l'entrainement d'un model

<blockquote>

Ne pas oublier de bien configurer le fichier de configuration.

</blockquote>

<p>&nbsp;</p>

# Configuration

## Example de fichier de configuration (_custom.yaml_)

```
path: D:\GABRIEL_Masson\DeepL\Dataset
train: D:\GABRIEL_Masson\DeepL\Dataset\train
test: D:\GABRIEL_Masson\DeepL\Dataset\test
val: D:\GABRIEL_Masson\DeepL\Dataset\valid

nc: 3

names: ["circle", "rectangle", "arrow"]
```