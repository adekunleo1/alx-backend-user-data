/**
 * Contains the miscellaneous route handlers.
 * @author Adekunle Ogunleye <https://github.com/adekunleo1>
 */
class AppController {
  static getHomepage(request, response) {
    response.status(200).send('Hello Holberton School!');
  }
}

export default AppController;
module.exports = AppController;
