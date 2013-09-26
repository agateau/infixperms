#!/bin/sh
set -e

SBDIR=/tmp/sandbox
rm -rf $SBDIR

mkdir $SBDIR

echo "Start infixperms on $SBDIR, then press ENTER"
read x

cd $SBDIR

touch .unison.tmp.zog
chmod 600 .unison.tmp.zog
mv .unison.tmp.zog zog

touch ../outside
chmod 600 ../outside
mv ../outside .
