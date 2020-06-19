####################################################################################################################################################
#
# The script aims to remove non-text characters in each sample. 
#
# Environment Requirement: Python 3.5, Anaconda3
# Date of Last Modified: 06/19/2020
# Author: Yingfei(Jeremy) Xiang
#
####################################################################################################################################################

import re
from sgmllib import SGMLParser
import sys,os
import nltk
from nltk.parse.stanford import StanfordDependencyParser, StanfordNeuralDependencyParser
from langdetect import detect

def main(argv):
  indir = argv[0]
  files = os.listdir(indir)

  numfiles = 0
  for filename in files:
    if not filename.endswith('.txt'):
      continue
    else:
      numfiles = numfiles + 1

  cnt = 0
  for filename in files:
     if not filename.endswith('.txt'):
      continue
     cnt = cnt + 1
     print('(%d/%d) - Processing %s' % (cnt,numfiles,filename))
     fname = os.path.join(indir,filename)
     text_file = open(fname,"r+")
     text = text_file.read()

     #-----remove html tags-----
     class TextExtracter(SGMLParser):
       def __init__(self):
         self.text = []
         SGMLParser.__init__(self)
       def handle_data(self, data):
         self.text.append(data)
       def getvalue(self):
         return ''.join(ex.text)
     ex = TextExtracter()
     ex.feed(text)
     text = ex.getvalue()
        
     #-----remove urls-----------------------
     Url_RE=re.compile(r'https?://[^\s<>"]+|www\.[^\s<>"]+')
     def remove_urls(text):
       return Url_RE.sub('',text)
     text = remove_urls(text)

     #------remove non-ascii characters------
     text = re.sub(r'[^\x00-\x7f]',r'', text)

     #-----remove urlLink--------------------
     text = text.replace("urlLink","")
     
     # #-------remove emoji--------------------
     # emoji_RE=re.compile(r'\*\s[a-z]+\s\*')
     # emoj_list = (':)',': )',':~',':-)',': - )',':-(',': - (',':(',': (',':B',':|','8-)',':<',':$',':X',': X',':Z',':\'(',':-|',': - |',':@',':P',': P',':D',': D',':O',':+','Cb',':Q',':T',',@P',',@-D',':d',',@o',':g','|-)',':!',':L',':>',',@f',':-S',',@x',',@@',',@!','xx','&-(','B-)','<@','@>',':-O',': - O','>-|','P-(',':\'|','X-)',':*','@x','8*','pd','<W>','@)','jj','@@','lvu','<L>','<O>','/[]','#-0','/[]','<&','&>','oY')
     # text=emoji_RE.sub('',text)
     # for i in xrange(len(emoj_list)):
     #  text=text.replace(emoj_list[i],'')

     #parse sentences and get valid sentences
     dep_parser = StanfordNeuralDependencyParser()
     sents = nltk.sent_tokenize(text)
     valid_sents = []
     invalid_sents = 0
     for sent in sents:
       try:
         parsed = dep_parser.raw_parse(sent)
         # Retain only english sentences
         if (detect(sent) == 'en'):
           valid_sents.append(sent)
         else:
           invalid_sents = invalid_sents + 1
       except:
         invalid_sents = invalid_sents + 1
     print('%d/%d sentences were valid' % (len(sents)-invalid_sents,len(sents)))
     text = ' '.join(valid_sents)
                
     text_file.close()
     if len(text) > 0:
       text_file = open(fname,"w")
       text_file.write(text)
       text_file.close()
     else:
       print('Deleting %s' % fname)
       os.remove(fname)

if __name__ == "__main__":
  main(sys.argv[1:])
