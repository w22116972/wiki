# Setup Gemini CLI with MCP servers

## Context

Why we need MCP servers when gemini cli is already able to access aws or k8s?
- provide deep, contextual domain knowledge: MCP servers improve model responses for specialized domains to reduce hallucinations and response quality
- access to latest documentation: foundation models may not be familiar with recent releases API, SDK etc. 

## List of recommended MCP servers

- docker
- github
- kubernetes
- [aws](https://github.com/awslabs/mcp)
    - aws-eks 
    - [aws-terraform](https://github.com/awslabs/mcp/blob/main/src/terraform-mcp-server)
    - [aws-documentation](https://github.com/awslabs/mcp/blob/main/src/aws-documentation-mcp-server)
        - `docker pull mcp/aws-documentation`
- [sequentialthinking](https://hub.docker.com/r/mcp/sequentialthinking)
    - `docker pull mcp/sequentialthinking`

## Steps

1. install MCP servers by `npm install` or `docker pull`
2. update `~/.gemini/settings.json`

### by docker

```
docker pull mcp/sequentialthinking
docker pull mcp/kubernetes
docker pull mcp/aws-documentation
```

### by npm

```

```

### update `~/.gemini/settings.json`

```json
    "mcpServers": {
        "sequentialthinking": {
            "command": "docker",
            "args": [
                "run",
                "-i",
                "--rm",
                "mcp/sequentialthinking"
            ]
        },
        "kubernetes": {
            "command": "docker",
            "args": [
                "run",
                "-i",
                "--rm",
                "mcp/kubernetes"
            ]
        }        
    }
```