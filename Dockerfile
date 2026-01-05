FROM python:3.14-alpine AS builder

RUN apk add --no-cache gcc musl-dev libffi-dev

ENV VENV=/opt/venv
RUN python -m venv $VENV
ENV PATH="$VENV/bin:$PATH"

WORKDIR /build
COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt

FROM python:3.14-alpine

RUN apk add --no-cache libffi

# Copy the virtual-env from builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy bot code
WORKDIR /app
COPY . .

RUN adduser -D -u 1000 bot
USER bot

ENTRYPOINT [ "python" , "bot.py" ]
