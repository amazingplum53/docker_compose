FROM nginx:latest

WORKDIR /etc/nginx/

COPY ./nginx.conf /etc/nginx/nginx.conf

COPY ./controller.sh /var/

