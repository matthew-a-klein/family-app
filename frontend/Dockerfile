# Use a more recent LTS version of Node.js
FROM node:16-alpine

# Set working directory
WORKDIR /app

# Add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# Install app dependencies
COPY package.json ./
COPY package-lock.json ./
RUN npm install --silent

# Add app
COPY . ./

# Start app
CMD ["npm", "start"]
