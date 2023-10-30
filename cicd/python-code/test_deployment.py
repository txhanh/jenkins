import subprocess

def test_deployment():
  """Tests if the application is deployed successfully."""

  # Get the output of the application.
  output = subprocess.check_output(["docker", "exec", "my-python-app", "python", "app.py"])

  # Assert that the application is running and returning the expected output.
  assert output == "Hello, world!"

if __name__ == "__main__":
  test_deployment()