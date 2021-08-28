FROM node:12.2.0-alpine

WORKDIR /DevLog

ENV PATH /node_modules/.bin:$PATH

COPY . .
RUN npm install 
RUN npm install react-scripts@3.0.1 -g

CMD ["npm", "start"]