#! /usr/bin/env bash
source venv/bin/activate
if [ -d "./emojifi_site/emojifi/analyzer/nltkdata" ];
then
echo "nltk is installed."
else
python -m nltk.downloader -d ./emojifi_site/emojifi/analyzer/nltkdata/ all
fi
