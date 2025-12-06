@echo off
pushd ..\..
docker compose up -d --build
popd
