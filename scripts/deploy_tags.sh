#!/bin/bash

curl --ftp-create-dirs -T stdm-*.tar.gz -u $FTP_USER:$FTP_PASSWORD ftp://$FTP_ADDRESS/tags/