# Use the official Rust image as a base
FROM rust:latest

# Install musl-tools and libssl-dev
RUN apt-get update \
    && apt-get install -y musl-tools libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /Jojos-Bizarre-API

# Copy the entire local directory into the container
COPY . .

# Install the necessary toolchain for the specified target
RUN rustup target add x86_64-unknown-linux-musl

# Install OpenSSL development headers
RUN apt-get update \
    && apt-get install -y pkg-config libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Build your Rust project
RUN cargo build

# Expose the port your application listens on
EXPOSE 3000

# Run your application
CMD ["cargo", "run", "--release"]
