# Error Handling

- use `panic!` for unrecoverable errors
- use `Result` for recoverable errors
  - `Result<T, E>`: `T` for meaningfully value, `E` for error
  - `Result<(), E>`, `Result<()>`: for those no need to return value

### Example: `panic!`

```rust
enum Result<T, E> {
    Ok(T),
    Err(E),
}

fn main() {
    let greeting_file_result = File::open("hello.txt");

    let greeting_file = match greeting_file_result {
        Ok(file) => file,
        Err(error) => match error.kind() {
            ErrorKind::NotFound => match File::create("hello.txt") {
                Ok(fc) => fc,
                Err(e) => panic!("Problem creating the file: {:?}", e),
            },
            other_error => {
                panic!("Problem opening the file: {:?}", other_error);
            }
        },
    };
}
```

### can use `expect(message)` to replace `panic!`

```rust
fn main() {
    let greeting_file = File::open("hello.txt")
        .expect("hello.txt should be included in this project");
}
```

### Example: `?`(Try Operator) propagate errors
- if function returns **only one error type** to represent all the ways a function might fail
- else use `match` to handle different error types

```rust
fn read_username_from_file() -> Result<String, io::Error> {
    let mut username = String::new();
    File::open("hello.txt")?.read_to_string(&mut username)?;
    Ok(username)
}
```

