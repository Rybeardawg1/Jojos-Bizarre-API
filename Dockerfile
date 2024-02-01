FROM messense/rust-musl-cross:x86_64-musl as builder
WORKDIR /Jojos-Bizarre-API
# Copy the source code
COPY . .
# Build the application
RUN cargo build --release --target x86_64-unknown-linux-musl

FROM scratch
COPY --from=builder /Jojos-Bizarre-API/target/x86_64-unknown-linux-musl/release/jojos-bizarre-api /usr/local/bin/jojos-bizarre-api
ENTRYPOINT ["/usr/local/bin/jojos-bbizarre-api"]
EXPOSE 3000