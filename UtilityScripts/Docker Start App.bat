@ECHO OFF
cd /d %dp0
cd ..
ECHO Starting local container
docker build -t fastapiexperimentation:localtest -f ./Docker/FastAPIExperimentation .
docker run -d -p 80:80 --name fastapi fastapiexperimentation:localtest
ECHO Press enter to stop local container
pause
docker stop fastapi
docker rm fastapi
docker image rm fastapiexperimentation:localtest
pause