FROM nginx:1.21-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
COPY localhost.crt /etc/nginx/conf.d
COPY localhost.key /etc/nginx/conf.d