task :dev do
    sh "docker-compose up --build"
end



task :shell do
    sh "docker compose exec processor /bin/bash"
end

task :test do
    sh "docker compose exec processor pytest -s"
end
