package controllers

import (
	"github.com/labstack/echo"
	"net/http"
)

func X(c echo.Context) error {
	return c.String(http.StatusOK, "Hello")
}