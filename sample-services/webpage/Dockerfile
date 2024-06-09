# Use an official Node.js runtime as the base image
FROM node:18

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install the application dependencies
RUN npm ci

# Copy the entire project directory to the working directory
COPY . .

# Build the Svelte application
RUN npm run build

# Install a lightweight web server (e.g., serve)
RUN npm install -g serve

# Expose the port on which the application will run
EXPOSE 5050

# Set the command to run the application
CMD ["serve", "-s", "public", "-l", "5050"]