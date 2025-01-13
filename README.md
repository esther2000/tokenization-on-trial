# Tokenization on Trial: The Case of Kalaallisut–Danish Legal Machine Translation

> **Abstract:**
> The strengths of subword tokenization have been widely demonstrated when applied to higher-resourced, morphologically simple languages. However, it is not self-evident that these results transfer to lower-resourced, morphologically complex languages. In this work, we investigate the influence of different subword segmentation techniques on machine translation between Danish and Kalaallisut, the official language of Greenland. We present the first semi-manually aligned parallel corpus for this language pair, and use it to compare subwords from unsupervised tokenizers and morphological segmenters. We find that Unigram-based segmentation both preserves morphological boundaries and handles out-of-vocabulary words adequately, but that this does not directly correspond to superior translation quality. We hope that our findings lay further groundwork for future efforts in neural machine translation for Kalaallisut.

## Note
This repository is currently under construction.


## Dataset
To generate the dataset used in our experiments:

```sh
bash scripts/run_all.sh
```

## Citation
If you use any contents from this repository for your work, we kindly ask you to cite our paper:
```
@inproceedings{ploeger2025tokenization,
  title={Tokenization on Trial: The Case of Kalaallisut--Danish Legal Machine Translation},
  author={Ploeger, Esther and Saucedo, Paola and Bjerva, Johannes and Kristensen-McLachlan, Ross Deans and Lent, Heather},
  booktitle={The 25th Nordic Conference on Computational Lingustics and 11th Baltic Conference on Human Language Technologies},
  year={2025}
}
```