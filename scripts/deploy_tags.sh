#!/bin/bash
zip -9 -r stdm-${TRAVIS_TAG}.zip stdm
curl --ftp-create-dirs -T stdm-*.zip -u $FTP_USER:$FTP_PASSWORD ftp://$FTP_ADDRESS/tags/