#! /usr/bin/env bash
ntlk_dir=/usr/local/lib/nltk_data
source venv/bin/activate
if [ -d "$ntlk_dir" ];
then
echo "nltk is installed."
else
python -m nltk.downloader -d $ntlk_dir all
fi
