FROM node:20

WORKDIR /app

COPY package.json .
RUN npm install

COPY server.js .
COPY views ./views

EXPOSE 3000

CMD ["node", "server.js"]
