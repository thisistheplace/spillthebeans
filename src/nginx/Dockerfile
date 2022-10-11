FROM nginx:latest

RUN mkdir /www
RUN mkdir /www/data

RUN rm /etc/nginx/nginx.conf
COPY nginx/nginx.conf /etc/nginx/
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/project.conf /etc/nginx/conf.d/

# Copy static files
COPY app/assets /www/data/assets