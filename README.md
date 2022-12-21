

# LAB - Class 28

## Project: Authentication & Production Server

### Author: Bayan bushnaq



### Setup

#### `.env` requirements (where applicable)
#### `django` 
#### `docker`
#### `pycopg3`



#### How to initialize/run your application (where applicable)

- e.g. `python manage.py runserver`
-      `python manage.py managemigration`
-      `python manage.py migrate`
-      `docker run project name `



#### Tests

- How do you run tests?
### python manage.py test
- Any tests of note?
### No.

### Insomnia tests
 * install insomnia from this link (https://insomnia.rest/)
 *  open the insomnia app then test the 'post' url (http://127.0.0.1:8000/api/v1/languages/)
    * ![without login](./assets/without%20login.png)
 * after login as admin : "username":"Bayan" , "password":"bushnaq1234"
    * ![after login](./assets/get%20after%20sign_in.png)
 * try to get by using access token
     * ![token](./assets/token.png)
 * try to post some fields using access token
     * ![post using access token](./assets/post%20using%20access%20token.png)
 * try to post field after access token expired  
    * ![expired token](./assets/post%20after%20access%20token%20expired.png)
* try to get the access token by refresh token
    * ![expired token](./assets/get%20the%20access%20token%20agter%20expired.png)



#### Pull Request Link:
##### [pull request](https://github.com/BayanBushnaq/Authentication-Production-Server/pull/1)
