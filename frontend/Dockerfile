#FROM node:14
#
#WORKDIR /frontend
#
#COPY ./package*.json /frontend/
#
#RUN npm install
#
#COPY . /frontend
#
#RUN npm run build
#
#EXPOSE 5173
#
##CMD ["npx", "serve", "-s", "dist", "-l", "5173"]
#CMD [ "npm", "run", "dev", "--", "--host", "0.0.0.0" ]
#

FROM node:lts-alpine
WORKDIR /frontend
RUN npm install -g vite
COPY . /frontend
RUN npm install
EXPOSE 5173
CMD [ "npm", "run", "dev", "--", "--host", "0.0.0.0" ]
