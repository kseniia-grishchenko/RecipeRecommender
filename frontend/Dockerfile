FROM node:14

WORKDIR /frontend

COPY ./package*.json /frontend/

RUN npm install -g serve

COPY . /frontend

RUN npm run build

EXPOSE 5173

CMD ["npx", "serve", "-s", "dist", "-l", "5173"]
