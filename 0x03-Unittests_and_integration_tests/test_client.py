#!/usr/bin/env python3
"""
Test the GithubOrgClient.org and returns the correct value
"""
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient  # Assuming GithubOrgClient is in client.py

class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('utils.get_json')
    def test_org(self, org, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        mock_get_json.return_value = {"org": org}
        client = GithubOrgClient(org)
        self.assertEqual(client.org, {"org": org})
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org}")

    def test_public_repos_url(self):
        """Test GithubOrgClient._public_repos_url"""
        with patch('client.GithubOrgClient.org', return_value={"repos_url": "https://api.github.com/orgs/test/repos"}):
            client = GithubOrgClient("test")
            self.assertEqual(client._public_repos_url, "https://api.github.com/orgs/test/repos")

    @patch('utils.get_json')
    @patch('client.GithubOrgClient._public_repos_url')
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test GithubOrgClient.public_repos"""
        mock_public_repos_url.return_value = "https://api.github.com/orgs/test/repos"
        mock_get_json.return_value = [{"name": "repo1"}, {"name": "repo2"}]

        client = GithubOrgClient("test")
        self.assertEqual(client.public_repos(), ["repo1", "repo2"])
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/test/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test GithubOrgClient.has_license"""
        client = GithubOrgClient("test")
        self.assertEqual(client.has_license(repo, license_key), expected)


class TestIntegrationGithubOrgClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up class with mocks"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        from fixtures import org_payload, repos_payload, expected_repos, apache2_repos

        cls.mock_get.side_effect = [
            MagicMock(json=MagicMock(return_value=org_payload)),
            MagicMock(json=MagicMock(return_value=repos_payload)),
        ]

    @classmethod
    def tearDownClass(cls):
        """Stop patcher"""
        cls.get_patcher.stop()

    @parameterized_class([
        ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    ])
    def test_public_repos(self, org_payload, repos_payload, expected_repos, apache2_repos):
        """Integration test for GithubOrgClient.public_repos"""
        client = GithubOrgClient("test")
        self.assertEqual(client.public_repos(), expected_repos)

    def test_public_repos_with_license(self):
        """Integration test for GithubOrgClient.public_repos with a specific license"""
        client = GithubOrgClient("test")
        self.assertEqual(client.public_repos(license="apache-2.0"), apache2_repos)
