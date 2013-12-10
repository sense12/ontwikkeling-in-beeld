server {

    listen 80;
    server_name localhost;


    location / {
         root /vagrant/www;
    }

    location = /api/ {
       proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
       proxy_set_header Host $host;

       proxy_pass http://127.0.0.1:8000/;
    }

    location ~ ^/api/(.+)$ {
       proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
       proxy_set_header Host $host;

       proxy_pass http://127.0.0.1:8000/$1;
    }

    error_page 500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }

}
