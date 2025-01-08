FROM nginx:1.27.1-alpine-slim

# RUN rm /etc/nginx/conf.d/default.conf -> temp
COPY nginx.conf /etc/nginx/conf.d

