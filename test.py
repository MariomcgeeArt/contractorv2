from app import app
from unittest import TestCase, main
from unittest.mock import patch
from bson.objectid import ObjectId


class AppTests(TestCase): 
    """Run tests on the Songs App."""
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    def test_home(self):
        result = self.app.get('/')

        # Check that status code is OK.
        self.assertEqual(result.status_code, 200)


    @patch('pymongo.collection.Collection.delete_one')
    def test_delete_playlist(self, mock_delete):
        form_data = {'_method': 'DELETE'}

        mock_bracelet= {
            'brand': 'gold',
            'size': '100'
        }
        mock_bracelet_id = ObjectId('5d55cffc4a3d4031f42827a3')
        result = self.app.post(f'/bracelets/{mock_bracelet_id}/delete', data=form_data)
        self.assertEqual(result.status, '302 FOUND')
        mock_delete.assert_called_with({'_id': mock_bracelet_id})



    @patch('pymongo.collection.Collection.find_one')
    def test_show_bracelet(self, mock_find):
        """Test showing a single bracelet."""
       

        mock_bracelet= {
            'brand': 'gold',
            'size': '100'
        }
        mock_bracelet_id = ObjectId('5d55cffc4a3d4031f42827a3')
        mock_find.return_value = mock_bracelet
        result = self.app.get(f'/bracelets/{mock_bracelet_id}')
        self.assertEqual(result.status, '200 OK')






if __name__ == '__main__':
    main()