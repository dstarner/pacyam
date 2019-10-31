COVERAGE_DIR:=htmlcov

.PHONY: test-coverage
test-coverage:
	py.test --cov=pacyam --cov-report html:$(COVERAGE_DIR) --cov-fail-under=60

.PHONY: lint
lint:
	pylint pacyam tests