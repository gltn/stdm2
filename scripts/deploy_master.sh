#!/bin/bash

curl --ftp-create-dirs -T stdm-*.zip -u $FTP_USER:$FTP_PASSWORD ftp://$FTP_ADDRESS/master/