# pull official base image
FROM node:14.18-alpine

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install app dependencies
COPY package.json ./
COPY package-lock.json ./
RUN npm install --silent
RUN npm install react-scripts@3.4.1 -g --silent
RUN export MapboxAccessToken=pk.eyJ1IjoiamRuaGl4IiwiYSI6ImNrd2s0NzF2ejFvb20yeW80NTlvenJ4OXMifQ.FxlxjZc-nN21l0s7N6EUwA

# add app
COPY . ./

ENV GENERATE_SOURCEMAP=false

# start app
CMD ["npm", "start"]