from lib.class_exercise import *
import pytest

diary_entry = DiaryEntry('Test Title', 'Test Contents')
diary_entry1 = DiaryEntry("50 words","Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi facilisis nisi at orci euismod, ac vehicula magna consectetur. Aenean ac metus elit. Nullam eleifend vitae nisl ut luctus. Praesent rhoncus eu turpis iaculis pellentesque. Ut diam odio, egestas eu ullamcorper vitae, malesuada sit amet lectus. Aenean sed efficitur est. Vivamus.")
diary_entry2 = DiaryEntry("200 words", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris odio odio, consectetur eu ante eu, tristique euismod diam. Nam condimentum consectetur massa vestibulum porttitor. Maecenas tempor, leo volutpat rutrum mattis, nibh quam dignissim nisl, sit amet vulputate augue nulla sit amet felis. Duis ultricies purus tortor, non convallis enim semper vehicula. Curabitur et dapibus odio. Donec hendrerit magna quam, vitae mollis mauris pharetra vitae. Nunc lacinia tellus metus, elementum faucibus justo pretium non. Donec ac luctus justo. Nullam luctus sit amet est vitae tempor. Vivamus sit amet elit non massa tempor volutpat. Morbi nec aliquam ligula. Etiam eget maximus libero. Sed faucibus ultricies turpis vel iaculis. Etiam consectetur ipsum ac erat rutrum auctor.Fusce vel est ac arcu tempor aliquam. Duis ac sodales nibh. Cras egestas molestie augue id pulvinar. Vivamus in tincidunt odio. Vivamus eu posuere mi. Cras aliquet nec nunc in fermentum. Donec dapibus eros lacus. Vestibulum tempus eros at elementum fringilla. Nullam vestibulum lectus ac iaculis rutrum. Integer sed mollis est, in volutpat purus. Donec non accumsan nisi. Nunc a augue eu felis dictum placerat non non mauris. Sed vestibulum diam eu augue pretium, non tristique tellus vulputate. Aliquam eu justo tempor, semper augue nec, pellentesque tortor.")

def test_instance_of_class():
    assert isinstance(diary_entry, DiaryEntry)

def test_instance_of_for_incorrect_datatype():
    with pytest.raises(Exception) as e:
        diary_entry_instance = DiaryEntry("title", 2)
    error_message = str(e.value)
    assert error_message == "Only strings are allowed!"

def test_formatting_an_entry():
    assert diary_entry.format() == "Test Title: Test Contents"
    
def test_count_words():
    assert diary_entry.count_words() == 4

def test_reading_time():
    assert diary_entry.reading_time(50) == "Less than a minute"
    assert diary_entry1.reading_time(50) == "1 minute"
    assert diary_entry2.reading_time(50) == "4 minutes"
    assert diary_entry1.reading_time(200) == "Less than a minute"
    assert diary_entry2.reading_time(200) == "1 minute"

def test_reading_time_for_incorrect_datatype():
    with pytest.raises(Exception) as e:
        diary_entry1.reading_time('hello')
    error_message = str(e.value)
    assert error_message == "Only integers are allowed!"

def test_reading_chunk():
    assert diary_entry1.reading_chunk(50, 1) == "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi facilisis nisi at orci euismod, ac vehicula magna consectetur. Aenean ac metus elit. Nullam eleifend vitae nisl ut luctus. Praesent rhoncus eu turpis iaculis pellentesque. Ut diam odio, egestas eu ullamcorper vitae, malesuada sit amet lectus. Aenean sed efficitur est. Vivamus."
    assert diary_entry1.contents == ""
    assert diary_entry2.reading_chunk(50, 1) == "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris odio odio, consectetur eu ante eu, tristique euismod diam. Nam condimentum consectetur massa vestibulum porttitor. Maecenas tempor, leo volutpat rutrum mattis, nibh quam dignissim nisl, sit amet vulputate augue nulla sit amet felis. Duis ultricies purus tortor, non convallis enim semper"
    assert diary_entry2.contents == " vehicula. Curabitur et dapibus odio. Donec hendrerit magna quam, vitae mollis mauris pharetra vitae. Nunc lacinia tellus metus, elementum faucibus justo pretium non. Donec ac luctus justo. Nullam luctus sit amet est vitae tempor. Vivamus sit amet elit non massa tempor volutpat. Morbi nec aliquam ligula. Etiam eget maximus libero. Sed faucibus ultricies turpis vel iaculis. Etiam consectetur ipsum ac erat rutrum auctor.Fusce vel est ac arcu tempor aliquam. Duis ac sodales nibh. Cras egestas molestie augue id pulvinar. Vivamus in tincidunt odio. Vivamus eu posuere mi. Cras aliquet nec nunc in fermentum. Donec dapibus eros lacus. Vestibulum tempus eros at elementum fringilla. Nullam vestibulum lectus ac iaculis rutrum. Integer sed mollis est, in volutpat purus. Donec non accumsan nisi. Nunc a augue eu felis dictum placerat non non mauris. Sed vestibulum diam eu augue pretium, non tristique tellus vulputate. Aliquam eu justo tempor, semper augue nec, pellentesque tortor."

def test_reading_chunk_for_incorrect_datatype():
    with pytest.raises(Exception) as e:
        diary_entry1.reading_chunk('hello', 2)
    error_message = str(e.value)
    assert error_message == "Only integers are allowed!"