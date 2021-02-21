#NODEJS
FROM node:14 as nodejs
ADD ./package.json /app/package.json
ADD ./webpack.config.js /app/webpack.config.js
ADD ./src /app/src
WORKDIR /app
RUN npm install
RUN npm run build

# NGINX
FROM nginx
COPY nginx/conf/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=nodejs /app/web /usr/share/nginx/html

WORKDIR /app