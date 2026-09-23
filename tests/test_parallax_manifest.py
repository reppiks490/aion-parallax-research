import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

from aion.parallax_manifest import scan_archives


class ManifestTests(unittest.TestCase):
    def test_preserves_physical_members_duplicate_headers_and_logical_rows(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "charts.zip"
            content = 'time,close,close,note\n1,2,3,"two\nlines"\n1,4,5,same-clock\n'
            with ZipFile(path, "w") as archive:
                archive.writestr("NQ, 20.csv", content)
                archive.writestr("copy/NQ, 20.csv", content)
                archive.writestr("__MACOSX/._NQ, 20.csv", "not a source")
            result = scan_archives([path])
            self.assertEqual(result["counts"]["physical_csv_members"], 2)
            self.assertEqual(result["counts"]["parsed_csv_members"], 2)
            self.assertEqual(result["counts"]["logical_data_rows"], 4)
            self.assertEqual(result["counts"]["unique_byte_contents"], 1)
            self.assertEqual(result["counts"]["records_in_exact_duplicate_groups"], 2)
            first, second = result["members"]
            self.assertNotEqual(first["physical_source_id"], second["physical_source_id"])
            self.assertEqual(first["headers"][2], {"position": 2, "name": "close"})
            self.assertEqual(first["duplicate_header_names"], ["close"])
            self.assertFalse(first["source_identity_verified"])
            self.assertFalse(result["execution_authorized"])

    def test_malformed_member_is_visible_and_not_counted_as_parsed(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.zip"
            with ZipFile(path, "w") as archive:
                archive.writestr("bad.csv", b"\xff\xfe")
            result = scan_archives([path])
            self.assertEqual(result["counts"]["physical_csv_members"], 1)
            self.assertEqual(result["counts"]["parsed_csv_members"], 0)
            self.assertEqual(result["members"][0]["status"], "parse_error")


if __name__ == "__main__":
    unittest.main()
