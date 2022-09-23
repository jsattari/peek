#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from logger import logger


def list_of_fields(*args) -> list:
    """
    Provides a list of available fields within a csv

    Values:
        data (list):    dataset that will contain list of fields

    Return (list):      a list of fields from dataset
    """

    try:
        output = [key for key in args[0][0].keys()]

        if len(output) > 0:
            logger.info("Succesfully returned list of outputs")
            return output

        else:
            logger.info(
                "No header fields could be parsed within dataset")
            raise ValueError("No header fields could be parsed within dataset")

    except KeyError:
        logger.info(
            "Something went wrong with loading the file for parsing")
        raise KeyError(
            "Something went wrong with loading the file for parsing")


def search(*args) -> list:
    """
    Filter data by choice of field and desired value

    Values:
        data (list):            dataset that will be filtered
        field (str):            field that will be used as basis for filtration
        filter_value (str):     value that will be used as the filter

    Return (list):              a list of dicts filtered by the desired value
    """

    if args[1][0] not in list_of_fields(args[0]):
        logger.info("Field value is not present in dataset")
        raise ValueError("Field value is not present in dataset")

    try:
        output = [struct for struct in args[0]
                  if struct[args[1][0]].lower() == args[1][1].lower()]

        if len(output) == 0:
            logger.info(
                "There is no value matching selected filter within dataset")
            raise IndexError(
                "There is no value matching selected filter within dataset")

        else:
            logger.info("Successfully returned hashmap of data")
            return output
    except KeyError as error:
        logger.info(error)
        return error


def head(*args) -> list:
    """
    Returns the first 5 rows of data as a preview

    Values:
        data (list):        dataset for preview

    Return (list):          list of first 5 rows of dataset
    """

    try:
        output = args[0][:5]
        logger.info("Sucessfully returned first 5 rows of data")
        return output
    except IndexError as error:
        logger.info("Insuffient data to be displayed")
        return error


def tail(*args) -> list:
    """
    Returns the last 5 rows of data as a preview

    Values:
        data (list):        dataset for preview

    Return (list):          list of first 5 rows of dataset
    """

    try:
        output = args[0][-5:]
        logger.info("Sucessfully returned last 5 rows of data")
        return output
    except IndexError as error:
        logger.info("Insuffient data to be displayed")
        return error
