#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      saad.bendaoud
#
# Created:     16/07/2019
# Copyright:   (c) saad.bendaoud 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from nltk.tokenize import word_tokenize
#from nltk.tokenize import toktok.ToktokTokenizer
def textProcessing(txt):
    list = word_tokenize(txt, language='french')


