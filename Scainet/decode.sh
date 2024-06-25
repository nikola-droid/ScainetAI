#!/bin/bash

export KALDI_ROOT=$HOME/kaldi

export PATH=$KALDI_ROOT/src/latbin:$KALDI_ROOT/src/online2bin:$KALDI_ROOT/src/lmbin:$KALDI_ROOT/src/rnnlmbin:$KALDI_ROOT/egs/wsj/s5/utils:$KALDI_ROOT/tools/openfst/bin:$PWD:$PATH
export LC_ALL=C

online2-wav-nnet3-latgen-faster \
      --word-symbol-table=graph/words.txt \
      --config=conf/model.conf \
      --config=conf/online.conf \
      am/final.mdl graph/HCLG.fst ark:decoder-test.utt2spk scp:decoder-test.scp ark:- |
    lattice-lmrescore --lm-scale=-1.0 ark:- 'fstproject --project_output=true rescore/G.fst |' ark:- |
    lattice-lmrescore-const-arpa --lm-scale=1.0 ark:- rescore/G.carpa ark:- |
    lattice-lmrescore-kaldi-rnnlm-pruned --lm-scale=0.5 --bos-symbol=709155 --eos-symbol=709156 --brk-symbol=709157 \
        --lattice-compose-beam=4.0 --acoustic-scale=1.0 --max-ngram-order=4 rescore/G.fst \
     'rnnlm-get-word-embedding rnnlm/word_feats.txt rnnlm/feat_embedding.final.mat -|' \
     rnnlm/final.raw ark:- ark:- | \
    lattice-align-words rescore/phones/word_boundary.int am/final.mdl ark:- ark:- |
    lattice-to-ctm-conf --frame-shift=0.03 --acoustic-scale=1.0 ark:- - |
    int2sym.pl -f 5 rescore/words.txt - -
