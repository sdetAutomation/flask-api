from messages.error_messages import error_message_helper


def test_messages_tc0001_error_message_helper():
    td_message = 'tc0001'
    expected_message = '{ "error": "tc0001."}'
    actual_message = error_message_helper(td_message)
    assert actual_message == expected_message
