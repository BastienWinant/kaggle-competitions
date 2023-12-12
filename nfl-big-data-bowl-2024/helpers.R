library(tidyverse)

import_file_to_dataframe <- function(file_path) {
  df <- read_csv(file_path, show_col_types = FALSE)
}

import_games <- function() {
  return(import_file_to_dataframe("data/games.csv"))
}

import_players <- function() {
  return(import_file_to_dataframe("data/players.csv"))
}

import_plays <- function() {
  return(import_file_to_dataframe("data/plays.csv"))
}

import_tackles <- function() {
  return(import_file_to_dataframe("data/tackles.csv"))
}

import_tracking <- function(week_number = NULL) {
  if (is.null(week_number)) {
    print("week number was not given")
  } else {
    df <- import_file_to_dataframe(str_glue("data/tracking_week_{week_number}.csv"))
    return(df)
  }
}