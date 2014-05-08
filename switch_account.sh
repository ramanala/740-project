#!/bin/bash

# general format: grep -rli 'old-word' * | xargs -i@ sed -i 's/old-word/new-word/g' @
grep -rli 'AP1093a59027e3c961f248d3ed0b227fb1' * | xargs -i@ sed -i 's/AP1093a59027e3c961f248d3ed0b227fb1/APcdc54402e77bd0aa98ab42bd5d045f89/g' @

grep -rli '9ef8d0cf4a2ba22bd95100f4c60f73f1' * | xargs -i@ sed -i 's/9ef8d0cf4a2ba22bd95100f4c60f73f1/7a0007278ebe72b311ca4d476c7a6abc/g' @

grep -rli 'ACd2d60924637e45d7da64057baee43362' * | xargs -i@ sed -i 's/ACd2d60924637e45d7da64057baee43362/AC3d6188091a9109165c89ae83c5d94d1b/g' @

grep -rli '17075023742' * | xargs -i@ sed -i 's/17075023742/16082345103/g' @
