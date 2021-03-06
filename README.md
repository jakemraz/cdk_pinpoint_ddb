
# Welcome to cdk_pinpoint_ddb project!

## Edit your configuration
Edit **lambda_fn/config.py** file.
```python
# config.py

PINPOINT_CONFIG = {
    'application_id': '<PUT_PINPOINT_APPLICATION_ID_HERE>'
}
```

## How to build and deploy
This is a blank project for Python development with CDK.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the .env
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .env
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .env/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .env\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip3 install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

Deploy this stack to your default AWS account/region
```
$ cdk deploy
```

# Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

# Sample payload
```json
{
  "segment": "<PUT YOUR SEGMENT NAME>",
  "title": "Hello",
  "message": "Echo Buds!",
  "category": "IT",
  "icon": "https://apprecs.org/ios/images/app-icons/256/6d/580990573.jpg",
  "image": "https://pplware.sapo.pt/wp-content/uploads/2019/09/Amazon_Echo_Buds_02.jpg"
}
```

Enjoy!
