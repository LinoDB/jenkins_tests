echo "Starting Jenkins Server..."
start http://localhost:8080/
java -jar jenkins.war --httpPort=8080