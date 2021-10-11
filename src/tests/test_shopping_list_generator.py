
from typing import List
from unittest.mock import mock_open, patch
import pytest
import shopping_list_generator.__main__


def configure_mock_open(mo, mock_file_contents: List[str]):
    write_mock = mock_open(read_data="")
    handlers = (mo.return_value, 
                *[mock_open(read_data=content).return_value for content in mock_file_contents],
                write_mock.return_value)
    mo.side_effect = handlers
    return mo, write_mock


class TestIntegrationCLITests:
    def test_should_fail_if_no_recipes_given(self):
        with pytest.raises(SystemExit) as wrapped_exception:
            shopping_list_generator.__main__.main(['main.py'])
        assert wrapped_exception.type == SystemExit
        assert wrapped_exception.value.code == 2

    def test_should_fail_if_recipe_does_not_exist(self):
        return_code = shopping_list_generator.__main__.main(['main.py', 'test_recipes/daassl'])
        # Should fail as recipe does not exist
        assert return_code == 1

    @patch("builtins.open", new_callable=mock_open, read_data="1 onion\n1 pepper\n1 lentil")
    def test_should_successfully_generate_shopping_list(self, mo):
        configured_mock_open, write_mock = configure_mock_open(mo, ['1 onion\n1 pepper\n1 spaghetti'])

        shopping_list_generator.__main__.main(['main.py', 'daal, spaghetti'])

        write_mock().write.assert_called_once_with("2 onion\n2 pepper\n1 lentil\n1 spaghetti")

    @patch("builtins.open", new_callable=mock_open, read_data="1 onion\n1 pepper\n1 lentil")
    def test_should_successfully_generate_shopping_list_and_handle_case(self, mo):
        configured_mock_open, write_mock = configure_mock_open(mo, ['1 Onion\n1 Pepper\n1 spaghetti'])

        shopping_list_generator.__main__.main(['main.py', 'daal, spaghetti'])

        write_mock().write.assert_called_once_with("2 onion\n2 pepper\n1 lentil\n1 spaghetti")

    @patch("builtins.open", new_callable=mock_open, read_data="1 onion\n1 pepper\n1 lentil")
    def test_should_successfully_handle_empty_lines(self, mo):
        configured_mock_open, write_mock = configure_mock_open(mo, ['1 onion\n\n1 pepper\n1 spaghetti\n\n\n'])

        shopping_list_generator.__main__.main(['main.py', 'daal, spaghetti'])

        write_mock().write.assert_called_once_with("2 onion\n2 pepper\n1 lentil\n1 spaghetti")
