# Pydantic Validation

FastHTTP integrates seamlessly with Pydantic to provide automatic type validation and data validation for API responses. This ensures type safety and data integrity when working with external APIs.

## What is Pydantic Validation?

Pydantic validation allows you to define data models that automatically validate and parse API responses. When you specify a response model, FastHTTP validates the response data against the model structure and type hints.

## Benefits

- **Type Safety**: Automatic type checking at runtime
- **Data Validation**: Ensures response data matches expected structure
- **IDE Support**: Better autocomplete and type hints in your IDE
- **Error Handling**: Clear validation error messages when data is invalid
- **Documentation**: Self-documenting API contracts
- **Serialization**: Automatic JSON conversion and parsing

## Using Response Models

Add the `response_model` parameter to any HTTP method decorator to enable automatic validation. The response data will be validated and returned as an instance of your Pydantic model.

```python
from fasthttp import FastHTTP
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str


app = FastHTTP()


@app.get(url="https://api.example.com/users/1", response_model=User)
async def get_user(resp) -> User:
    data = resp.json()
    return data
```

## Model Features

### Field Validation

Use Pydantic's `Field` to add constraints and validation rules to your model fields. This allows you to enforce business rules directly in your data models.

### Custom Validators

Implement custom validation logic using Pydantic's validator decorators. This gives you full control over how data is validated.

### Nested Models

Define complex data structures with nested Pydantic models. This is useful for APIs that return hierarchical data.

### Type Coercion

Pydantic automatically converts compatible types, such as converting string numbers to integers or parsing date strings into datetime objects.

## Common Use Cases

- **API Clients**: Type-safe clients for external APIs
- **Data Validation**: Ensuring data integrity from third-party services
- **Type Hints**: Better IDE autocomplete and error detection
- **Documentation**: Clear data structure definitions
- **Error Prevention**: Catch data issues early in development

## Validation Errors

When validation fails, Pydantic raises a `ValidationError` with detailed information about which fields failed and why. This helps you quickly identify and fix data issues.

## Best Practices

1. Define separate models for input and output when needed
2. Use descriptive field names and add descriptions
3. Leverage Field constraints for business rules
4. Implement custom validators for complex logic
5. Always use type hints for better IDE support

---

For more examples, see the [Examples](examples.md) section.
