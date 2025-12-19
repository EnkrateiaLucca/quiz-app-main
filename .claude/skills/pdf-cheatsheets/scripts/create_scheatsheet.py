#!/usr/bin/env python3
"""
Cheatsheet Creator - Generate PDF cheatsheets from structured content.

Usage:
    python create_cheatsheet.py --title "Title" --sections sections.json --output out.pdf
    
Or import and use directly:
    from create_cheatsheet import create_cheatsheet
    create_cheatsheet("Title", sections_list, "output.pdf")
"""

import argparse
import json
from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle


def create_cheatsheet(title: str, sections: list[dict], output_path: str) -> str:
    """
    Create a PDF cheatsheet from structured sections.
    
    Args:
        title: The cheatsheet title
        sections: List of dicts with 'heading' and 'items' keys
                  Example: [{"heading": "Basics", "items": ["item1", "item2"]}]
        output_path: Where to save the PDF
    
    Returns:
        Path to the created PDF
    """
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        topMargin=0.5 * inch,
        bottomMargin=0.5 * inch,
        leftMargin=0.5 * inch,
        rightMargin=0.5 * inch
    )
    
    # Define styles
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CheatsheetTitle',
        parent=styles['Title'],
        fontSize=20,
        spaceAfter=12,
        textColor=HexColor('#1a1a2e')
    )
    
    heading_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading2'],
        fontSize=12,
        spaceBefore=10,
        spaceAfter=6,
        textColor=HexColor('#16213e'),
        backColor=HexColor('#e8e8e8'),
        borderPadding=4
    )
    
    item_style = ParagraphStyle(
        'BulletItem',
        parent=styles['Normal'],
        fontSize=9,
        leading=12,
        leftIndent=12,
        bulletIndent=0,
        spaceBefore=2,
        spaceAfter=2
    )
    
    # Build content
    story = []
    
    # Title
    story.append(Paragraph(title, title_style))
    story.append(Spacer(1, 6))
    
    # Sections
    for section in sections:
        heading = section.get('heading', 'Section')
        items = section.get('items', [])
        
        # Section heading
        story.append(Paragraph(heading, heading_style))
        
        # Items as bullet points
        for item in items:
            bullet_text = f"• {item}"
            story.append(Paragraph(bullet_text, item_style))
        
        story.append(Spacer(1, 6))
    
    # Build PDF
    doc.build(story)
    
    return output_path


def main():
    parser = argparse.ArgumentParser(
        description='Create a PDF cheatsheet from structured content'
    )
    parser.add_argument(
        '--title', '-t',
        required=True,
        help='Title for the cheatsheet'
    )
    parser.add_argument(
        '--sections', '-s',
        required=True,
        help='Path to JSON file containing sections'
    )
    parser.add_argument(
        '--output', '-o',
        default='cheatsheet.pdf',
        help='Output PDF path (default: cheatsheet.pdf)'
    )
    
    args = parser.parse_args()
    
    # Load sections from JSON
    sections_path = Path(args.sections)
    if not sections_path.exists():
        print(f"Error: Sections file not found: {args.sections}")
        return 1
    
    with open(sections_path) as f:
        sections = json.load(f)
    
    # Create the cheatsheet
    output = create_cheatsheet(args.title, sections, args.output)
    print(f"Created cheatsheet: {output}")
    
    return 0


if __name__ == '__main__':
    exit(main())