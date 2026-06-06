# --- Stage 1: Build & Dependency Resolution ---
FROM python:3.11-alpine AS builder

WORKDIR /build

# Install dependencies into a localized wheelhouse folder
COPY app/requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /build/wheels flask

# --- Stage 2: Hardened Production Runtime ---
FROM python:3.11-alpine AS runner

# Principal Architecture: Enforce Non-Root UID execution
RUN addgroup -g 10001 appgroup && \
    adduser -u 10001 -G appgroup -h /home/appuser -D appuser

WORKDIR /app

# Pull dependencies from builder stage safely
COPY --from=builder /build/wheels /wheels
RUN pip install --no-cache /wheels/*

# Copy code resources and shift filesystem ownership boundaries
COPY main.py .
RUN chown -R appuser:appgroup /app

# Switch executing context away from default root access
USER 10001

EXPOSE 8080

ENV APP_ENV=Production

CMD ["python", "main.py"]